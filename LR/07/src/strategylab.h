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
    int labNumber;
    QString comments;

public:
    explicit StrategyLab(int, QObject* parent = nullptr);
    ~StrategyLab();
    bool check(QList<QString>);
    bool hasComments() const { return comments.isEmpty(); }
    QString getComments() const { return comments; }

private:
    void getCode();

};

#endif // STARTEGYLAB_H
