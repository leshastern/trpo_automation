#ifndef CONTROLEXCEPTION_H
#define CONTROLEXCEPTION_H

#include <QException>

class ControlException : public QException
{
private:
    bool code;
    QString message;
public:
    explicit ControlException(QString, bool);
    void raise() const override { throw *this; }
    ControlException *clone() const override { return new ControlException(*this); }

    bool getCode() const { return code; }
    QString getMessage() const { return message; }
};

#endif // CONTROLEXCEPTION_H
