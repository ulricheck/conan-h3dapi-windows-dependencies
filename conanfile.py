import os
from conans import ConanFile, CMake, tools

class H3DAPIWinDepsConan(ConanFile):
    name = "h3dapi_windows_dependencies"
    version = "2.3"
    settings = "os", "compiler"
    url = "https://github.com/ulricheck/h3dapi_windows_dependencies"


    def build(self):
        if self.settings.os == "Windows": # check for MSVC??
            vs_version = int(str(self.settings.compiler.version))
            if vs_version == 10:
                folder = 'vs2010'
            elif vs_version == 12:
                folder = 'vs2013'
            elif vs_version == 14:
                folder = 'vs2015'
            elif vs_version > 14:
                folder = 'vs2017'
            else:
                raise Exception('Unsupported MSVC Compiler %s' % vs_version)

            repo_url = "https://www.h3dapi.org:8090/External/%s/" % folder
            self.run("git svn clone %s source" % repo_url)
        else:
            raise Exception("Binary does not exist for these settings")

    def package(self):
        self.copy("*", src="source/include") 
        self.copy("*", src="source/bin32") 
        self.copy("*", src="source/bin64") 
        self.copy("*", src="source/lib32") 
        self.copy("*", src="source/lib64") 

    def package_info(self):  # still very useful for package consumers
        self.env_info.H3D_EXTERNAL_ROOT = self.package_folder
