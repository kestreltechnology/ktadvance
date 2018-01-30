# ------------------------------------------------------------------------------
# Script to export the C Analyzer Analysis Results to the SCARF (SWAMP Common Assessment Result Format) format
# Author: John Schroeder
# ------------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2017 Kestrel Technology LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ------------------------------------------------------------------------------

import argparse
import time
import uuid
import platform
import os
from third_party.ScarfXmlWriter import ScarfXmlWriter

import advance.reporting.ProofObligations as RP
import advance.util.printutil as UP

from advance.util.IndexedTable import IndexedTableError
from advance.app.CApplication import CApplication


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='directory that holds the semantics directory')
    parser.add_argument('file', help='name of the file to write the SCARF output to')
    parser.add_argument('--includesafe',
                        help='include proof obligations that were not found to be issues',
                        action='store_true')
    args = parser.parse_args()
    return args


def project_proofobligation_export_scarf(capp, outputFile, includeSafeProofObligations):

    # make a directory to hold all the output files
    # name it after the project directory (we're in semantics/ktadvance at this point)
    odir = capp.path
    for i in range(0, 2):
        odir = os.path.split(odir)[0]
    odir = os.path.basename(odir)
    if not os.path.exists(odir):
        os.makedirs(odir)

    ppos = capp.get_ppos()
    spos = capp.get_spos()

    sw = ScarfXmlWriter(outputFile, 2, False)
    initialData = \
    {
        "assess_fw": "N/A",
        "assess_fw_version": "N/A",
        "assessment_start_ts": time.time(),
        "build_fw": "N/A",
        "build_fw_version": "N/A",
        "build_root_dir": capp.path[:capp.path.index("semantics")],
        "package_name": odir,
        "package_version": "N/A",
        "package_root_dir": capp.path[:capp.path.index("semantics")],
        "parser_fw": "KTAdvance SCARF Writer",
        "parser_fw_version": "0.5",
        "platform_name": platform.system() + "_" + platform.release(),
        "tool_name": "KTAdvance",
        "tool_version": "0.5",
        "uuid": uuid.uuid4()
    }

    errors = sw.CheckStart(initialData)
    if errors:
        for error in errors:
            print error
        return

    sw.AddStartTag(initialData)

    for po in ppos + spos:
        if includeSafeProofObligations or po.status != 'safe':

            cweId = []
            tag = po.potype.get_predicate().get_tag()
            if tag == 'not-null':
                cweId.append('476')
            #elif tag == 'null':
            #    cweId.append('?')
            elif tag == 'valid-mem':
                cweId.append('825')
            #elif tag == 'global-mem':
            #    cweId.append('?')
            elif tag == 'allocation-base':
                cweId.append('822')
            #elif tag == 'type-at-offset':
            #    cweId.append('?')
            elif tag == 'lower-bound':
                cweId.append('823')
            elif tag == 'upper-bound':
                cweId.append('823')
            elif tag == 'index-lower-bound':
                cweId.append('125')
            elif tag == 'index-upper-bound':
                cweId.append('125')
            elif tag == 'initialized':
                cweId.append('665')
            elif tag == 'initialized-range':
                cweId.append('131')
            elif tag == 'cast':
                cweId.append('704')
            elif tag == 'pointer-cast':
                cweId.append('704')
            elif tag == 'signed-to-unsigned-cast':
                cweId.append('195')
            elif tag == 'unsigned-to-signed-cast':
                cweId.append('196')
            elif tag == 'not-zero':
                cweId.append('369')
            elif tag == 'null-terminated':
                cweId.append('170')
            #elif tag == 'non-negative':
            #    cweId.append('?')
            elif tag == 'int-underflow':
                cweId.append('191')
            elif tag == 'int-overflow':
                cweId.append('190')
            #elif tag == 'width-overflow':
            #    cweId.append('?')
            elif tag == 'ptr-lower-bound':
                cweId.append('786')
            elif tag == 'ptr-upper-bound':
                cweId.append('788')
            elif tag == 'ptr-upper-bound-deref':
                cweId.append('788')
            #elif tag == 'common-base':
            #    cweId.append('?')
            #elif tag == 'common-base-type':
            #    cweId.append('?')
            elif tag == 'format-string':
                cweId.append('133')
            #elif tag == 'no-overlap':
            #    cweId.append('?')
            #elif tag == 'global-mem':
            #   cweId.append('?')
            #elif tag == 'value-constraint':
            #    cweId.append('?')
            #elif tag == 'precondition':
            #    cweId.append('?')

            bug = \
            {
                "BugGroup": po.status,
                "BugCode": tag,
                "BugMessage": po.explanation,
                #"BugSeverity": None,
                #"ResolutionSuggestion": None,
                "AssessmentReportFile": capp.path + "/",
                "BuildId": "1.0",
                #"InstanceLocation":
                #{
                #    "Xpath": None,
                #    "LineNum":
                #    {
                #        "Start": None,
                #        "End": None
                #    }
                #},
                "CweIds": cweId,
                #"ClassName": None,
                #"Methods": None,
                "BugLocations":
                [
                    {
                        "SourceFile": po.location.get_file(),
                        "StartLine": str(po.location.get_line()),
                        "EndLine": str(po.location.get_line()),
                        "StartColumn": str(po.location.get_byte()),
                        "EndColumn": str(po.location.get_byte()),
                        "primary": "true",
                        "Explanation": po.location.__str__()
                    }
                ]
            }

            errors = sw.CheckBug(bug)
            for error in errors:
                print error

            if not errors:
                sw.AddBugInstance(bug)

    sw.AddSummary()
    sw.AddEndTag()
    sw.Close()


if __name__ == '__main__':

    args = parse()

    cpath = args.path
    if not os.path.isdir(cpath):
        print(UP.cpath_not_found_err_msg(cpath))
        exit(1)

    sempath = os.path.join(cpath, 'semantics')

    if not os.path.isdir(sempath):
        print(UP.semantics_not_found_err_msg(cpath))
        exit(1)

    capp = CApplication(sempath)
    try:
        project_proofobligation_export_scarf(capp, args.file, args.includesafe)
    except IndexedTableError as e:
        print(e.msg)

