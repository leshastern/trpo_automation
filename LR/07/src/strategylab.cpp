#include "strategylab.h"

/**
 * @brief Конструктор
 * @param objectFromServer
 * @param parent
 */
StrategyLab::StrategyLab(int givenNumber, QObject* parent)
    : QObject(parent),
      labNumber(givenNumber)
{}

bool StrategyLab::check(QList<QString> code) {
    return false;
}

/**
 * @brief Деструктор
 */
StrategyLab::~StrategyLab()
{
    // TODO дописать
}
