from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = f'mirror3{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzipmirror3{CMD_INDEX}'
        self.ZipMirrorCommand = f'zipmirror3{CMD_INDEX}'
        self.CancelMirror = f'cancel3{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall3{CMD_INDEX}'
        self.ListCommand = f'list3{CMD_INDEX}'
        self.SearchCommand = f'search3{CMD_INDEX}'
        self.StatusCommand = f'status3{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users3{CMD_INDEX}'
        self.AuthorizeCommand = f'auth3{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauth3{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo3{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo3{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restart3{CMD_INDEX}'
        self.StatsCommand = f'stats3{CMD_INDEX}'
        self.HelpCommand = f'help3{CMD_INDEX}'
        self.LogCommand = f'log3{CMD_INDEX}'
        self.CloneCommand = f'clone3{CMD_INDEX}'
        self.CountCommand = f'count3{CMD_INDEX}'
        self.WatchCommand = f'watch3{CMD_INDEX}'
        self.ZipWatchCommand = f'zipwatch3{CMD_INDEX}'
        self.QbMirrorCommand = f'qbmirror3{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'qbunzipmirror3{CMD_INDEX}'
        self.QbZipMirrorCommand = f'qbzipmirror3{CMD_INDEX}'
        self.DeleteCommand = f'del3{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f'leechset3{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb3{CMD_INDEX}'
        self.LeechCommand = f'leech3{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleech3{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleech3{CMD_INDEX}'
        self.QbLeechCommand = f'qbleech3{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbunzipleech3{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbzipleech3{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatch3{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatch3{CMD_INDEX}'
        self.RssListCommand = f'rsslist{CMD_INDEX}'
        self.RssGetCommand = f'rssget{CMD_INDEX}'
        self.RssSubCommand = f'rsssub{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset{CMD_INDEX}'

BotCommands = _BotCommands()
