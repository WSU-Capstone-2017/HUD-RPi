import QtQuick 2.0

Rectangle {
    width: 228; height: 114
    color: "blue"

    Text {
        id: onlineText
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        font.bold: true
        color: "white"
        text: "Navigation Online"
        horizontalAlignment: Text.AlignHCenter
    }
}