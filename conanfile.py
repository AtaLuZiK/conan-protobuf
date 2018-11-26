import os
from os import path

from conans import CMake, ConanFile, tools


class ProtobufConan(ConanFile):
    name = "protobuf"
    version = "3.5.1"
    license = "MIT"
    url = "https://github.com/AtaLuZiK/conan-protobuf"
    description = "Protocol Buffers - Google's data interchange format"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "with_zlib": [True, False],             # Build with zlib support
        "unicode": [True, False],
    }
    default_options = (
        "shared=False",
        "with_zlib=True",
        "unicode=False",
    )
    generators = "cmake"
    requires = "zlib/1.2.8@conan/stable"

    @property
    def zip_folder_name(self):
        return "%s-%s" % (self.name, self.version)

    def source(self):
        zip_name = "%s-cpp-%s.tar.gz" % (self.name, self.version)
        tools.download("https://github.com/google/protobuf/releases/download/v%s/protobuf-cpp-%s.tar.gz" % (self.version, self.version), zip_name)
        tools.check_md5(zip_name, "ca0d9b243e649d398a6b419acd35103a")
        tools.unzip(zip_name)
        os.unlink(zip_name)
        with tools.chdir(self.zip_folder_name):
            tools.replace_in_file("cmake/CMakeLists.txt", "project(protobuf C CXX)",
                '''project(${PACKAGE_NAME} C CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')
            tools.replace_in_file("cmake/CMakeLists.txt", "protobuf_SOURCE_DIR", "CMAKE_CURRENT_SOURCE_DIR")
            tools.replace_in_file("cmake/install.cmake", "protobuf_SOURCE_DIR", "CMAKE_CURRENT_SOURCE_DIR")
            tools.replace_in_file("cmake/install.cmake", "  if(EXISTS \"${_extract_from}\")", '''  if(EXISTS "${_extract_from}")
    file(COPY "${_extract_from}" DESTINATION "${_extract_to}")''')
            tools.replace_in_file("cmake/install.cmake", "  if(EXISTS \"${_file_from}\")", '''  if(EXISTS "${_file_from}")
    file(COPY "${_file_from}" DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/${_file_path}")''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["protobuf_WITH_ZLIB"] = "ON" if self.options.with_zlib else "OFF"
        cmake.definitions["protobuf_UNICODE"] = "ON" if self.options.unicode else "OFF"
        cmake.definitions["protobuf_MSVC_STATIC_RUNTIME"] = "OFF"
        cmake.definitions["protobuf_BUILD_TESTS"] = "OFF"
        cmake.definitions["protobuf_BINARY_DIR:PATH"] = path.abspath("bin")
        cmake.configure(source_folder=path.join(self.zip_folder_name, "cmake"))
        cmake.build()

    def package(self):
        if self.settings.os == "Windows":
            self.copy("*.exe", dst="bin", src="bin")
            self.copy("*.dll", dst="bin", src="bin")
            self.copy("*.lib", dst="lib", src="lib")
        else:
            self.copy("js_embed", dst="bin", src="bin")
            self.copy("protoc", dst="bin", src="bin")
            self.copy("*.so*", dst="lib", src="lib")
            self.copy("*.a", dst="lib", src="lib")
        self.copy("*.h", dst="include", src="include")
        self.copy("*.proto", dst="include", src="include")
        self.copy("*", dst="cmake", src="cmake")

    def package_info(self):
        self.cpp_info.libs = ["protobuf"]
