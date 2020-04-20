#ifndef FUNCTIONAL_H
#define FUNCTIONAL_H

#include <QObject>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QJsonDocument>
#include <QJsonObject>

/**
 * @brief Класс для получения листинга кода с GitHub
 */
class Functional : public QObject
{
    Q_OBJECT

public:
    QNetworkReply *reply;

private:
    QNetworkAccessManager *manager;
    QString headerData;

public:
    explicit Functional(QObject *parent = nullptr);
    ~Functional();
    void getContentFromGithub();
    void dataProcessing();
    void getLinkToFile();
};

#endif // FUNCTIONAL_H
