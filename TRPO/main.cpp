#include <QCoreApplication>
#include "strategylab.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    StrategyLab lab;

    return a.exec();
}
