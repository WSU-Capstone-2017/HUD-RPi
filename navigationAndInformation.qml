import QtQuick 2.0

Rectangle {
    width: 228; height: 114
    color: "red"

    Text {
        id: navigationAndInfoText
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        font.bold: true
        color: "white"
        text: "Navigation & Car Information \n Split Screen"
        horizontalAlignment: Text.AlignHCenter
    }
}