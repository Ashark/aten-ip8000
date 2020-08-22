Files purpose
- multiple-clicker - see description inside file
- srvrkeys - see description inside file

Window rules for KDE
- TeamViewer viewer window ignore global shortcuts.kwinrule
- IP8000 WinClient Video Settings not minimizable.kwinrule
- IP8000 WinClient viewer window ignore global shortcuts.kwinrule<br>
Names are speaking.<br>
I make ignore global shortcuts not only to pass local host binded shortcuts, such as alt+tab and f12, but also to be able to drag windows in remote system with alt+mouse.<br>
For TeamViewer matching window I use "— TeamViewer" as a substing, so it only matches viewer window itself. And also I use teamwiewer window class, to avoid possible detections for other applications.<br>
For IP8000 WinClient matching window I use "- WinClient" as a substing, so it only matches viewer window itself. And also I use iclient.exe wine window class, to avoid possible detections for other applications.<br>
Video Settings window is minimizable in wine, but not in Windows os. It is _really_ annoying, because viewer window becomes unusable, and you cannot understand what happened, because Video Settings is not shown in the taskbar panel even when minimized.<br>
I will report this bug to wine later. Interestingly, the same application (WinClient) has at the same time a working unminimizable window - virtual keyboard.

Window action group
- ctrl+alt+fx handlers window action.khotkeys<br>
This is not hotkeys, but window actions. See srvrkeys file. Currently window matching functionality in kde window actions is partly broken. When I use window class matching, it stops triggering. So for now I just use title matching. I did not reported it yet.<br>
https://bugs.kde.org/show_bug.cgi?id=401391 Bug 401391 - Window detection function does not work  
Another kde bug here. Changing comment string does not activate Apply button, so you need to edit some window matching rule, then press apply, and then revert unwanted change of editing window matching rule.
