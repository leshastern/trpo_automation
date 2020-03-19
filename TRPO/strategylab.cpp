#include "strategylab.h"

StrategyLab::StrategyLab(QObject* parent)
    : QObject(parent)
{
    server = new TcpServer();
}
