# conan-protobuf

Conan package for [protobuf](https://github.com/google/protobuf)

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/conan-community).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[ ![Download](https://api.bintray.com/packages/zimmerk/conan/protobuf%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/protobuf%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-protobuf.svg?branch=release%2F3.5.1)](https://travis-ci.org/AtaLuZiK/conan-protobuf)|[![Build status](https://ci.appveyor.com/api/projects/status/flv8fo7msmelnba0/branch/release/3.5.1?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-protobuf/branch/release/3.5.1)|

## Reuse the packages

### Basic setup

```
conan install protobuf/3.5.1@zimmerk/stable
```

### Project setup

```
[requires]
protobuf/3.5.1@zimmerk/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
