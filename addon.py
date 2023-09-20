import xbmcaddon
import xbmcvfs
import subprocess

addonPath = xbmcaddon.Addon('script.steam.menu').getAddonInfo('path')

startSteamCommand = xbmcaddon.Addon('script.steam.menu').getSettingString('start-steam')
stopKodiCommand = xbmcaddon.Addon('script.steam.menu').getSettingString('stop-kodi')
restartKodiCommand = xbmcaddon.Addon('script.steam.menu').getSettingString('restart-kodi')

logFile = xbmcvfs.translatePath('special://temp/steam.log')

subprocess.Popen([
    '/bin/bash', 
    addonPath + 'resources/bin/steam.sh', 
    startSteamCommand, 
    stopKodiCommand, 
    restartKodiCommand, 
    logFile
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
