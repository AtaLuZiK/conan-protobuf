find_path(PROTOBUF_INCLUDE_DIR NAMES google/protobuf/message.h PATHS ${CONAN_INCLUDE_DIRS_PROTOBUF})
find_library(PROTOBUF_LITE_LIBRARY NAMES libprotobuf-lite PATHS ${CONAN_LIB_DIRS_PROTOBUF})
find_library(PROTOBUF_LIBRARY NAMES libprotobuf PATHS ${CONAN_LIB_DIRS_PROTOBUF})
find_library(PROTOC_LIBRARY NAMES libprotoc PATHS ${CONAN_LIB_DIRS_PROTOBUF})
find_program(PROTOC_EXECUTABLE NAMES protoc PATHS ${CONAN_BIN_DIRS_PROTOBUF})

# Create imported target protobuf::libprotobuf-lite
add_library(protobuf::libprotobuf-lite INTERFACE IMPORTED)
target_include_directories(protobuf::libprotobuf-lite INTERFACE ${PROTOBUF_INCLUDE_DIR})
target_link_libraries(protobuf::libprotobuf-lite INTERFACE ${PROTOBUF_LITE_LIBRARY})

# Create imported target protobuf::libprotobuf
add_library(protobuf::libprotobuf INTERFACE IMPORTED)
target_include_directories(protobuf::libprotobuf INTERFACE ${PROTOBUF_INCLUDE_DIR})
target_link_libraries(protobuf::libprotobuf INTERFACE ${PROTOBUF_LIBRARY} "ZLIB::ZLIB")

# Create imported target protobuf::libprotoc
add_library(protobuf::libprotoc INTERFACE IMPORTED)
target_include_directories(protobuf::libprotobuf INTERFACE ${PROTOBUF_INCLUDE_DIR})
target_link_libraries(protobuf::libprotobuf INTERFACE ${PROTOC_LIBRARY} "protobuf::libprotobuf")

# Create imported target protobuf::protoc
add_executable(protobuf::protoc IMPORTED)
set_target_properties(protobuf::protoc PROPERTIES
  IMPORTED_LOCATION ${PROTOC_EXECUTABLE}
)

mark_as_advanced(PROTOBUF_INCLUDE_DIR PROTOBUF_LITE_LIBRARY PROTOBUF_LIBRARY PROTOC_LIBRARY PROTOC_EXECUTABLE)

message("** protobuf found by Conan!")
set(PROTOBUF_FOUND TRUE)
message("   - includes: ${PROTOBUF_INCLUDE_DIR}")
message("   - protobuf::libprotobuf-lite libraries ${PROTOBUF_LITE_LIBRARY}")
message("   - protobuf::libprotobuf libraries: ${PROTOBUF_LIBRARY} ZLIB::ZLIB")
message("   - protobuf::libprotoc libraries: ${PROTOC_LIBRARY} ${PROTOBUF_LIBRARY} ZLIB::ZLIB")
message("   - protobuf::protoc executable: ${PROTOC_EXECUTABLE}")
