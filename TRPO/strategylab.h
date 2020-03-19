#ifndef STARTEGYLAB_H
#define STARTEGYLAB_H

#include "tcpserver.h"

class StrategyLab: public QObject
{
    Q_OBJECT
public:
    explicit StrategyLab(QObject* parent = nullptr);

private:
    TcpServer * server;
};

#endif // STARTEGYLAB_H
