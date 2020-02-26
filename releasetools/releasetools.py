def FullOTA_InstallEnd(info):
	info.script.AppendExtra('ifelse(is_mounted("/system"), unmount("/system"));')
	info.script.AppendExtra('mount("ext4", "EMMC", "/dev/block/platform/dw_mmc/by-name/SYSTEM", "/system", "");')
	info.script.AppendExtra('run_program("rm", "/system/vendor");')
	info.script.AppendExtra('run_program("mkdir", "/system/vendor");')
	info.script.AppendExtra('unmount("/system");')
