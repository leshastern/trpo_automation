#include "controlexception.h"

ControlException::ControlException(QString thrownMessage, bool thrownCode)
    : message(thrownMessage),
      code(thrownCode)
{}
