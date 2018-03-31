#!/usr/bin/python

#  Copyright 2016 Brandon G. Klein
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import sys
import math
#from lxml import etree
from xml.etree import ElementTree as etree

###################Handle errors#############################################################
def error(error_level, message):
    if error_level == 0:
        return
    elif error_level == 1:
        print(message)
    else:
        print(message)
        sys.exit(1)

##########################################################################################
class ScarfXmlWriter:
    
##################Initialize Writer##################################################
    def __init__(self, output, error_level=1, pretty_enable=1):
#       try:
#           self.output = open(output, "w")
#       except IOError:
#           print('cannot open file')
#           sys.exit(1)
        self.output = output
        self.filetype = 1
        try:
            output.write()
            self.filetype = 0
        except AttributeError:
            self.output = open(output, 'w')
        #self.output = output
        if error_level == 1 or error_level == 0:
            self.error_level = error_level
        else:
            self.error_level = 2
        self.pretty = 0
        self.bodyType = ""
        self.start = 0
        self.pretty = pretty_enable
        self.encoding = "UTF-8"

        self.bugID = 1
        self.metricID = 1

        self.metricSummaries = {}
        self.bugSummaries = {}

    def _output_write(self, str_or_bytes):

        if isinstance(str_or_bytes, bytes):
            self.output.write(str_or_bytes.decode('UTF-8'))
        elif isinstance(str_or_bytes, str):
            self.output.write(str_or_bytes)

    ###########################encoding access/mutate#######################################
    def GetEncoding(self):
        return self.encoding

    def SetEncoding(self, encoding):
        self.encoding = encoding

#########################Returns file#######################################################
    def GetHandle(self):
        return self.output

######################Returns current set error level######################################################
    def GetErrorLevel(self):
        return self.error_level

#######################Pretty Print Options##########################################################
    def GetPrettyPrint(self):
        return self.pretty

    def SetPrettyPrint(self, pretty_enable):
        self.pretty = pretty_enable

####################Allows change of error level############################################################
    def SetErrorLevel(self, error_level):
        if error_level == 1:
            self.error_level = 1
        elif error_level == 0:
            self.error_level = 0
        elif error_level == 2:
            self.error_level = 2

#######################Write a start tag######################################

    def AddStartTag(self, initial_details):

        if self.error_level != 0:
            if self.start:
                print("Scarf file already open\n")
                if self.error_level == 2:
                    sys.exit(1)
            errors = self.CheckStart(initial_details)
            for error in errors:
                print(error)
            if errors and self.error_level == 2:
                sys.exit(1)
        self.start = 1
        self.bodyType = "body"
        self.metricSummaries = {}
        self.bugSummaries = {}

        writer = self.output
        writer.write("<?xml version=\"1.0\" encoding=\"%s\"?>\n" % (self.encoding))
        writer.write("<AnalyzerReport assess_fw=\"%s\" assess_fw_version=\"%s\" assessment_start_ts=\"%s\" build_fw=\"%s\" build_fw_version=\"%s\" build_root_dir=\"%s\" package_name=\"%s\" package_root_dir=\"%s\" package_version=\"%s\" parser_fw=\"%s\" parser_fw_version=\"%s\" platform_name=\"%s\" tool_name=\"%s\" tool_version=\"%s\" uuid=\"%s\">\n" % (
            initial_details['assess_fw'],
            initial_details['assess_fw_version'],
            initial_details['assessment_start_ts'],
            initial_details['build_fw'],
            initial_details['build_fw_version'],
            initial_details['build_root_dir'],
            initial_details['package_name'],
            initial_details['package_root_dir'],
            initial_details['package_version'],
            initial_details['parser_fw'],
            initial_details['parser_fw_version'],
            initial_details['platform_name'],
            initial_details['tool_name'],
            initial_details['tool_version'],
            initial_details['uuid']))

        return self

####################Write a bug instance#########################################################

    def AddBugInstance(self, bugHash):
        #Check for req elmts
        if self.error_level != 0:
            if self.bodyType == "summary":
                print("Summary already written. Invalid Scarf\n")
                if self.error_level == 2:
                    sys.exit(1)
            errors = self.CheckBug(bugHash)
            for error in errors:
                print(error)
            if errors and self.error_level == 2:
                sys.exit(1)

        # byte count info
        byte_count = 0
        initial_byte_count = 0
        initial_byte_count = self.output.tell()

        #Addbug
        bug = etree.Element("BugInstance")
        bug.set("id", "%s" % self.bugID)

        if "ClassName" in bugHash:
            className = etree.SubElement(bug, "ClassName")
            className.text = bugHash["ClassName"]

        if "Methods" in bugHash:
            methods = etree.SubElement(bug, "Methods")
            methodID = 1
            for method in bugHash["Methods"]:
                wrtMethod = etree.SubElement(methods, "Method")
                wrtMethod.text = method["name"]
                wrtMethod.set("id", "%s" % methodID)
                if method["primary"]:
                    primary = "true"
                else:
                    primary = "false"
                wrtMethod.set("primary", primary)

        if "BugLocations" in bugHash:
            if len(bugHash["BugLocations"]) >= 1:
                bugLocations = etree.SubElement(bug, "BugLocations")
                locID = 1
                for location in bugHash["BugLocations"]:
                    if location["primary"]:
                        primary = "true"
                    else:
                        primary = "false"
                    wrtLocation = etree.SubElement(bugLocations, "Location")
                    wrtLocation.set("id", "%s" % locID)
                    wrtLocation.set("primary", "%s" % primary)
                    for req in ["SourceFile"]:
                        locSubElement = etree.SubElement(wrtLocation, req)
                        locSubElement.text = "%s" % location[req]
                    for opt in ["StartColumn", "Explantion", "EndColumn", "StartLine", "EndLine"]:
                        if opt in location:
                            locSubElement = etree.SubElement(wrtLocation, opt)
                            locSubElement.text = "%s" % location[opt]
                    locID = locID + 1

        if "CweIds" in bugHash:
            for cweid in bugHash["CweIds"]:
                cwe = etree.SubElement(bug, "CweId")
                cwe.text = "%s" % cweid

        for bugElt in ["BugGroup", "BugCode", "BugRank", "BugSeverity"]:
            if bugElt in bugHash:
                eltSub = etree.SubElement(bug, bugElt)
                eltSub.text = bugHash[bugElt]

        bugMessage = etree.SubElement(bug, "BugMessage")
        bugMessage.text = "%s" % bugHash["BugMessage"]

        if "ResolutionSuggestion" in bugHash:
            resolution = etree.SubElement(bug, "ResolutionSuggestion")
            resolution.text = "%s" % bugHash["ResolutionSuggestion"]

        bugTrace = etree.SubElement(bug, "BugTrace")
        buildID = etree.SubElement(bugTrace, "BuildId")
        buildID.text = "%s" % bugHash["BuildId"]
        assessment = etree.SubElement(bugTrace, "AssessmentReportFile")
        assessment.text = bugHash["AssessmentReportFile"]
        if "InstanceLocation" in bugHash:
            instanceLoc = bugHash["InstanceLocation"]
            instance = etree.SubElement(bugTrace, "InstanceLocation")
            if "Xpath" in instanceLoc:
                xpath = etree.SubElement(instance, "Xpath")
                xpath.text = instanceLoc["Xpath"]
            if "LineNum" in instanceLoc:
                linenum = instanceLoc["LineNum"]
                line = etree.SubElement(instance, "LineNum")
                start = etree.SubElement(line, "Start")
                start.text = "%s" % linenum["Start"]
                end = etree.SubElement(line, "End")
                end.text = "%s" % linenum["End"]
        if self.pretty:
            self._output_write(etree.tostring(bug,
                                              encoding=self.encoding,
                                              pretty_print=True))
        else:
            self._output_write(etree.tostring(bug, encoding=self.encoding))
        bug.clear()
        self.bugID = self.bugID + 1

        # more byte count info
        final_byte_count = self.output.tell()
        byte_count = final_byte_count - initial_byte_count

        #group bugs for summary
        if "BugGroup" in bugHash:
            group = bugHash["BugGroup"]
        else:
            group = "undefined"

        if "BugCode" in bugHash:
            code = bugHash["BugCode"]
        else:
            code = "undefined"

        if code in self.bugSummaries:
            if group in self.bugSummaries[code]:
                summary = self.bugSummaries[code][group]
                summary["count"] = summary["count"] + 1
                summary["bytes"] = summary["bytes"] + byte_count
                self.bugSummaries[code][group] = summary
            else:
                self.bugSummaries[code][group] = {"count": 1, "bytes": byte_count}
        else:
            self.bugSummaries[code] = {}
            self.bugSummaries[code][group] = {"count": 1, "bytes": byte_count}

        bug.clear()
        return self


###########Writer a metric##################################################

    def AddMetric(self, metricHash):

        if self.error_level != 0:
            if self.bodyType == "summary":
                print("Summary already written. Invalid Scarf\n")
                if self.error_level == 2:
                    sys.exit(1)
            errors = self.CheckMetric(metricHash)
            for error in errors:
                print(error)
            if errors and self.error_level == 2:
                sys.exit(1)

        metric = etree.Element("Metric")
        metric.set("id", "%s" % self.metricID)

        loc = etree.SubElement(metric, "Location")
        source = etree.SubElement(loc, "SourceFile")
        source.text = metricHash["SourceFile"]

        for optMetr in ["Class", "Method"]:
            if optMetr in metricHash:
                opt = etree.SubElement(metric, optMetr)
                opt.text = metricHash[optMetr]

        for reqMetr in ["Type", "Value"]:
            req = etree.SubElement(metric, reqMetr)
            req.text = "%s" % metricHash[reqMetr]
        if self.pretty:
            self._output_write(etree.tostring(metric, encoding=self.encoding,
                                              pretty_print=True))
        else:
            self._output_write(etree.tostring(metric, encoding=self.encoding))
        self.metricID = self.metricID + 1

        metricType = metricHash["Type"]
        if metricType in self.metricSummaries:
            summary = self.metricSummaries[metricType]
            summary["Count"] = summary["Count"] + 1
            if metricType != "language" and "Sum" in summary:
                try:
                    value = float(metricHash["Value"])
                    summary["SumOfSquares"] = summary["SumOfSquares"] + value*value
                    summary["Sum"] = summary["Sum"] + value
                    if value > summary["Maximum"]:
                        summary["Maximum"] = value
                    if value < summary["Minimum"]:
                        summary["Minimum"] = value
                except ValueError:
                    try:
                        del summary["SumOfSquares"]
                        del summary["Sum"]
                        del summary["Maximum"]
                        del summary["Minimum"]
                    except KeyError:
                        pass
                except TypeError:
                    try:
                        del summary["SumOfSquares"]
                        del summary["Sum"]
                        del summary["Maximum"]
                        del summary["Minimum"]
                    except KeyError:
                        pass

            self.metricSummaries[metricType] = summary

        else:
            if metricType == "language":
                self.metricSummaries[metricType] = {"Count": 1}
            else:
                try:
                    value = float(metricHash["Value"])
                    summary = {"Count": 1, "Sum": value, "Maximum": value,
                               "Minimum": value, "SumOfSquares": value*value}
                    self.metricSummaries[metricType] = summary
                except ValueError:
                    self.metricSummaries[metricType] = {"Count": 1}

        metric.clear()
        return self

############Add summary from written elements##############################################################
    def AddSummary(self):

        if self.bugSummaries:
            self.bodyType = "summary"
            summaries = etree.Element("BugSummary")
            for code in self.bugSummaries:
                for group in self.bugSummaries[code]:
                    # summary = self.bugSummaries[code][group]
                    # codeBranch = etree.SubElement(summaries, code)
                    # groupBranch = etree.SubElement(codeBranch, group)
                    # groupBranch.set("count", "%s" % summary["count"])
                    # groupBranch.set("bytes", "%s" % summary["bytes"])
                    summary = self.bugSummaries[code][group]
                    summary_xml_element = etree.SubElement(summaries, 'BugCategory')
                    summary_xml_element.set("group", group)
                    summary_xml_element.set("code", code)
                    summary_xml_element.set("count", "%s" % summary["count"])
                    summary_xml_element.set("bytes", "%s" % summary["bytes"])
            self._output_write(etree.tostring(summaries, encoding=self.encoding))
                                              #pretty_print=True))

        if self.metricSummaries:
            self.bodyType = "summary"
            summaries = etree.Element("MetricSummaries")
            for metric in self.metricSummaries:
                summary = self.metricSummaries[metric]
                metricSummary = etree.SubElement(summaries, "MetricSummary")
                metricType = etree.SubElement(metricSummary, "Type")
                metricType.text = metric
                metricCount = summary["Count"]
                count = etree.SubElement(metricSummary, "Count")
                count.text = "%s" % metricCount

                if "Sum" in summary:
                    metricSum = summary["Sum"]
                    metricSumofSquares = summary["SumOfSquares"]
                    average = metricSum / metricCount

                    denominator = metricCount * (metricCount - 1)
                    squareOfSum = metricSum * metricSum
                    stdDeviation = 0
                    if denominator != 0:
                        stdDeviation = math.sqrt((metricSumofSquares * metricCount - squareOfSum) / denominator)

                    for sumElt in ["Sum", "SumOfSquares", "Minimum", "Maximum"]:
                        element = etree.SubElement(metricSummary, sumElt)
                        element.text = "%s" % summary[sumElt]

                    metricAverage = etree.SubElement(metricSummary, "Average")
                    metricAverage.text = "%s" % average

                    metricStdDeviation = etree.SubElement(metricSummary, "StandardDeviation")
                    metricStdDeviation.text = "%s" % stdDeviation
            if self.pretty:
                self._output_write(etree.tostring(summaries, encoding=self.encoding,
                                                  pretty_print=True))
            else:
                self._output_write(etree.tostring(summaries, encoding=self.encoding))
            summaries.clear()
            return self


#######################Add end tag for analyzer report###########################################
    def AddEndTag(self):
        if self.error_level != 0:
            if not self.start:
                print("Scarf file already closed\n")
                if self.error_level == 2:
                    sys.exit(1)
        self.start = 0
        self._output_write("</AnalyzerReport>")
        return self

    def Close(self):
        if self.start:
            self._output_write("</AnalyzerReport>")
        if self.filetype == 1:
            self.output.close()
        self = None
        return self

    def CheckStart(self, initial_details):
        errors = []
        for reqAttr in ["tool_name", "tool_version", "uuid"]:
            if reqAttr not in initial_details:
                errors.append("Required attribute: %s not found when creating startTag" % reqAttr)
        return errors

    def CheckMetric(self, metricHash):
        errors = []
        for reqElt in ["Value", "Type", "SourceFile"]:
            if reqElt not in metricHash:
                errors.append("Required element: %s could not be found for Metric" % (reqElt))
        return errors

    def CheckBug(self, bugHash):
        errors = []
        for reqElt in ["BugLocations", "BugMessage", "BuildId", "AssessmentReportFile"]:
            if reqElt not in bugHash:
                errors.append("Required element: %s could not be found in BugInstance" % (reqElt))
        if "Methods" in bugHash:
            methodID = 1
            methodPrimary = 0
            for method in bugHash["Methods"]:
                if "primary" not in method:
                    errors.append("Required attribute: primary not found for Method: %s in BugInstance" % (methodID))
                elif (method["primary"]):
                    if (methodPrimary):
                        errors.append("Misformed Element: More than one primary Method found in BugInstance");
                    else:
                        methodPrimary = 1
                if "name" not in method:
                    error.append("Required text: name not found for Method: %s in BugInstance" % (methodID))
                methodID = methodID + 1
    #       if not methodPrimary :
    #               errors.append("Misformed Element: No primary Method found in  BugInstance: %s.");

        if "BugLocations" in bugHash:   
            locPrimary = 0
            locID = 1
            for location in bugHash["BugLocations"]:
                if "primary" not in location:
                    errors.append("Required attribute: primary not found for Location: %s in BugInstance" % (locID))
                elif (location["primary"]):
                    if (locPrimary):
                       errors.append("Misformed Element: More than one primary Location found in BugInstance");
                    else:
                        methodPrimary = 1
                for reqLocElt in ["SourceFile"]:
                    if reqLocElt not in location:
                        errors.append("Required Element: %s could not be found for Location: %s in BugInstance" % (reqLocElt, locID))
                for optNum in ["StartLine", "EndLine", "StartColumn", "EndColumn"]:
                    if optNum in location:
                        if not location[optNum].isdigit():
                            errors.append("Wrong value type: $optLocElt child of BugLocation in BugInstance %s requires a positive integer.")
    #       if not locPrimary :
    #           errors.append("Misformed Element: No primary Location found in  BugInstance: %s.");
            locID = locID + 1

        if "CweIds" in bugHash:
            for cweid in bugHash["CweIds"]:
                if not cweid.isdigit():
                    errors.append("Wrong value type: CweID expected to be a positive integer in BugInstance %s.")

        if "InstanceLocation" in bugHash:
            if "LineNum" in bugHash["InstanceLocation"]:
                line_num = bugHash["InstanceLocation"]["LineNum"]
                if "Start" not in line_num:
                    errors.append("Required element missing: Could not find Start child of a LineNum in BugInstance")
                elif not line_num["Start"].isdigit():
                    errors.append("Wrong value type: Start child of LineNum requires a positive integer BugInstance")
                if "End" not in line_num:
                    errors.append("Required element missing: Could not find End child of a LineNum BugInstance")
                elif not line_num["End"].isdigit():
                    errors.append("Wrong value type: End child of LineNum requires a positive integer BugInstance")
            elif "Xpath" not in bugHash["InstanceLocation"]:
                errors.append("Misformed Element: Neither LineNum or Xpath children were present in InstanceLocation BugInstance")
        return errors


