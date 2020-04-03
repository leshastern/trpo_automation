#ifndef STARTEGYLAB_H
#define STARTEGYLAB_H

#include <QObject>
#include <QJsonObject>

/**
 * @brief Класс для проверки лабораторных работ
 *  по паттерну 'Стратегия'
 */
class StrategyLab: public QObject
{
    Q_OBJECT

private:
    QString code;
    QJsonObject object;

public:
    explicit StrategyLab(QJsonObject, QObject* parent = nullptr);
    ~StrategyLab();
    bool check();

private:
    void getCode();

};

#endif // STARTEGYLAB_H
