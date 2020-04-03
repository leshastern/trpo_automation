#include <QtTest>

// add necessary includes here

class temp : public QObject
{
    Q_OBJECT

public:
    temp();
    ~temp();

private slots:
    void test_case1();

};

temp::temp()
{

}

temp::~temp()
{

}

void temp::test_case1()
{

}

QTEST_APPLESS_MAIN(temp)

#include "tst_temp.moc"
