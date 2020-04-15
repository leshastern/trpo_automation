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
    QString link;
    QString secretToken;

public:
    explicit Functional(QString linkFromServer, QObject *parent = nullptr);
    void getContentFromGithub();
    void dataProcessing();
    void getLinkToFile();

private:
    QString authorize();
};

#endif // FUNCTIONAL_H
