#!/usr/bin/env python

from checkUtil import working_directory


class GradleParser(object):
    """

    This class will take a gradle file and returns a parsed Dictionary format
    """
    dictionary_list = ["outside"]
    gradle_dict = dict()


    def __init__(self,gradle_dir):
        with working_directory(gradle_dir):
            self.file = open("build.gradle","r")

    def parse(self):
        current_entry = object()
        for line in self.file:
            if line in ['\n', '\r\n']:
                pass
            if "//" in line:
                pass
            elif "{" in line.strip():
                arg,sep = line.strip().split(" ")
                self.dictionary_list.append(arg)
                self.gradle_dict[arg] = dict()
                current_entry = self.gradle_dict[arg]
            elif "{" and "}" not in line.strip():
                if(len(self.gradle_dict) == 0):
                    self.gradle_dict["outside"] = dict()
                current_entry = self.gradle_dict[self.dictionary_list[len(self.dictionary_list)-1]]
                args = line.strip().split(" ")
                if(len(args) == 2):
                    current_entry[args[0]] = args[1]
                elif(len(args)> 2):
                    for i in range(1,len(args)):
                        current_entry[args[0]] = args[i]
            elif "}" in line.strip():
                current_entry = self.dictionary_list.pop()

        return self.gradle_dict


