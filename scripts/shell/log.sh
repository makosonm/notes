#!/bin/bash
#
# 在Shell中进行日志的打印 有下面两种使用方式
#
# 方式一: 指定日志输入
#
# LOG_FILEPATH=$(pwd)/mako.log
# source log.sh
# 
# infolog "This test"       # 日志输入到指定mako.log 中
# errorlog "This test too"  # 日志输出到 mako.log.wf 中
#
# 方式二: 直接引入不指定LOG_FILEPATH
# 会查找当前目录下是否存在 log 或 logs 目录，不存在的话直接输出到console中
# 存在会以执行的shell脚本名称命名日志名.log .log.wf
# 
# source log.sh
# 
# infolog "方式二 查找当前执行目录下是否有log或logs目录没有直接输出的console中"
# errorlog "方式二 查找当前执行目录下是否有log或logs目录没有直接输出的console中"
#

if [ "$LOG_FILEPATH" != "" ]; then
  _logname=$(basename $LOG_FILEPATH)
  _logdir=${LOG_FILEPATH%/*}
  _logpath=$LOG_FILEPATH
else
  _logname=$(basename $0).log
  _logdir=./log && test -d ./logs && _logdir=./logs
  _logpath=${_logdir}/${_logname}
fi

_logrotate=14
_script=$0
_logpathwf=${_logpath}.wf
_log_initflag=1

_initlog() {
  if [ ! -d "$_logdir" ]; then
    _logpath=/dev/stdout && _logpathwf=/dev/stderr
  fi
}

_writelog() {
  _loglevel=$1
  if [ $1 == "" ]; then
    _loglevel="INFO"
  fi

  _logmsg="$2"
  if [ "$_logmsg" == "" ]; then
    _logmsg= "NULL"
  fi

  _logstamp=$(date +%Y%m%d-%H:%M:%S)

  if [ "$_loglevel" == "STDOUT" ]; then
    echo "${_logstamp} ${_loglevel} : ${_logmsg}"
    return
  fi

  if [ ! -d "$_logdir" ]; then
    if [ "$_loglevel" == "INFO" ] || [ "$_loglevel" == "DEBUG" ]; then
      echo "${_logstamp} ${_loglevel} : ${_logmsg}"
    else
      echo "${_logstamp} ${_loglevel} : ${_logmsg}" 1>&2
    fi
  else
    if [ "$_loglevel" == "INFO" ] || [ "$_loglevel" == "DEBUG" ]; then
      echo "${_logstamp} ${_loglevel} : ${_logmsg}" >>${_logpath}
    else
      echo "${_logstamp} ${_loglevel} : ${_logmsg}" >>${_logpathwf}
    fi
  fi
}

setlogpath() {
  _logpath=$1
  _logname=$(basename $_logpath)
  _logdir=${_logpath%/*}
  _logpathwf=${_logpath}.wf

  _initlog
}

stdoutlog() {
  _writelog "STDOUT" "$1"
}

debuglog() {
  _writelog "DEBUG" "$1"
}

infolog() {
  _writelog "INFO" "$1"
}

noticelog() {
  _writelog "NOTICE" "$1"
}

warnlog() {
  _writelog "WARNING" "$1"
}

errorlog() {
  _writelog "ERROR" "$1"
}

fatallog() {
  _writelog "FATAL" "$1"
}

criticallog() {
  _writelog "CRITICAL" "$1"
}

_initlog
