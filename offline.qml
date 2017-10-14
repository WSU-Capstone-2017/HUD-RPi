import QtQuick 2.0

Rectangle {
    width: 228; height: 114
    color: "orange"

    Text {
        id: navigationAndInfoText
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        font.bold: true
        color: "white"
        text: "Navigation Offline"
        horizontalAlignment: Text.AlignHCenter
    }
}