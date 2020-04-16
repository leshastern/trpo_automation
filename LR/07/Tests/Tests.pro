QT += testlib
QT -= gui
QT += network
QT += xml
SOURCES += \
    ../src/functional.cpp \
    ../src/strategylab.cpp \
    ../src/tcpserver.cpp \
    TestTcp.cpp

HEADERS += \
    ../src/functional.h \
    ../src/strategylab.h \
    ../src/tcpserver.h \
    TestTcp.h


