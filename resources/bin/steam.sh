#!/bin/bash

start_steam="$1"
stop_kodi="$2"
restart_kodi="$3"
log_file="$4"

function log() {
	echo "$@" >> $log_file;
}

if [ -f "$log_file" ]; then
    mv "${log_file}" "${log_file}.old"
	log "Replacing log file..."
fi

log "Stopping kodi with ${stop_kodi}";
$stop_kodi >> "$log_file" 2>&1;

log "Starting steam with ${start_steam}";
$start_steam >> "$log_file" 2>&1

log "Restarting kodi with ${restart_kodi}";
$restart_kodi
