#include "strategylab.h"

/**
 * @brief Конструктор
 * @param objectFromServer
 * @param parent
 */
StrategyLab::StrategyLab(QJsonObject objectFromServer, QObject* parent)
    : QObject(parent),
      object(objectFromServer)
{
    this->getCode();
}

/**
 * @brief Метод для извлечения основного кода программы
 *  из доставленного Json объекта
 * @throws QString
 */
void StrategyLab::getCode()
{
    if (object.contains("code")) {
        this->code = object.value("code").toString();
    }

    throw QString("Переданный Json объект не содержит поля 'code'");
}

/**
 * @brief Деструктор
 */
StrategyLab::~StrategyLab()
{
    // TODO дописать
}
