CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
PROJECT(vision_module)

INCLUDE_DIRECTORIES(
include
)

#########Opencv####################
set(OpenCV_DIR ${PROJECT_SOURCE_DIR}/3rdpart/opencv-3.1.0-install/share/OpenCV)
set(use_libs 
opencv_core
opencv_highgui
opencv_imgproc
opencv_imgcodecs
opencv_optflow
opencv_tracking
opencv_videoio
opencv_face
opencv_objdetect
cvface_api
opencv_video
json_linux-gcc-4.8_libmt
mysqlclient
pthread)

IF(NOT "${OpenCV_DIR}" EQUAL "")
	MESSAGE("Using OpenCV from " ${OpenCV_DIR})
ENDIF(NOT "${OpenCV_DIR}" EQUAL "")

find_package(OpenCV)
include_directories(${OpenCV_INCLUDE_DIRS})
link_directories(${OpenCV_LIBRARY_DIRS})
#link_directories(${OpenCV_INSTALL_PATH}/lib)
#MESSAGE("OpenCV_libs " ${OpenCV_INSTALL_PATH})
#MESSAGE("OpenCV_incs " ${OpenCV_INCLUDE_DIRS})
#LINK_DIRECTORIES(${PROJECT_SOURCE_DIR}/3rdpart)


#############gtk###################

find_package(PkgConfig)
if(PKG_CONFIG_FOUND)
    pkg_check_modules(GTK "gtk+-2.0")
endif()
#link_directories(${LIBMYSQLCLIENT_LIBRARY_DIRS})
#include_directories({LIBMYSQLCLIENT_INCLUDE_DIRS})

#############face lib##############

include_directories(${PROJECT_SOURCE_DIR}/3rdpart/xxx/include)
link_directories(${PROJECT_SOURCE_DIR}/3rdpart/xxx/libs/linux-x86_64)

#############Json lib##############

include_directories(${PROJECT_SOURCE_DIR}/3rdpart/jsoncpp-src-0.5.0/include)
link_directories(${PROJECT_SOURCE_DIR}/3rdpart/jsoncpp-src-0.5.0/libs/linux-gcc-4.8)
					
################mysql##############

#execute_process(COMMAND mysql_config --cflags OUTPUT_VARIABLE MYSQL_CFLAGS)
#execute_process(COMMAND mysql_config --libs   OUTPUT_VARIABLE MYSQL_LIBS)
#string(STRIP ${MYSQL_CFLAGS} MYSQL_CFLAGS)
#string(STRIP ${MYSQL_LIBS} MYSQL_LIBS)
#message("flags:" ${MYSQL_CFLAGS})
#message("libs: " ${MYSQL_LIBS})
set(MySQL_DIR ${PROJECT_SOURCE_DIR}/3rdpart/cmake)
find_package(MySQL REQUIRED)
include_directories(${MYSQL_INCLUDE_DIRS})

##################CURL#############

find_package(CURL)
if(CURL_FOUND)
    include_directories(${CURL_INCLUDE_DIR})
else(CURL_FOUND)
    message(FATAL_ERROR "CURL library not found")
endif(CURL_FOUND)

###################################
#                                 #
#                                 #
###################################

AUX_SOURCE_DIRECTORY(src SRC_LIST)

ADD_EXECUTABLE(${PROJECT_NAME} ${SRC_LIST})

if(GTK_FOUND)
    #target_compile_options(${PROJECT_NAME} ${MYSQL_CFLAGS})
    TARGET_LINK_LIBRARIES(${PROJECT_NAME} ${use_libs} ${GTK_LIBRARIES} ${MYSQL_LIBRARIES} ${CURL_LIBRARY})
    add_definitions(${GTK_CFLAGS} ${GTK_FLAGS_OTHER}  -fpermissive)

else(GTK_FOUND)
    TARGET_LINK_LIBRARIES(${PROJECT_NAME} ${use_libs})
endif(GTK_FOUND)


