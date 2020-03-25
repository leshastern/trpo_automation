#include "strategylab.h"

StrategyLab::StrategyLab(QJsonObject objectFromServer, QObject* parent)
    : QObject(parent),
      object(objectFromServer)
{
    this->getCode();
}

void StrategyLab::getCode()
{
    if (object.contains("code")) {
        this->code = object.value("code").toString();
    }

    throw QString("Переданный Json объект не содержит поля 'code'");
}

StrategyLab::~StrategyLab()
{

}
