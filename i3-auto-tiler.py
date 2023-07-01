import i3ipc


def on_window_new(i3, event):
    tree = i3.get_tree()
    focused = tree.find_focused()

    if focused.rect.width > focused.rect.height:
        focused.command('focus child; splith')
    else:
        focused.command('focus child; splitv')


i3 = i3ipc.Connection()
i3.on('window::new', on_window_new)
i3.main()
