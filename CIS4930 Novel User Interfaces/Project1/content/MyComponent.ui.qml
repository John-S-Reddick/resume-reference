import QtQuick 6.5

Rectangle {
    color: Constants.backgroundColor

    Text {
        text: qsTr("Hello Project1")
        anchors.centerIn: parent
        font.family: Constants.font.family
    }
}
