import QtQuick 2.0

Rectangle {
    width: 228; height: 114
    color: "green"

    Text {
        id: navigationAndInfoText
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        font.bold: true
        color: "white"
        text: "Car Information"
        horizontalAlignment: Text.AlignHCenter
    }
}