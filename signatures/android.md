* android version: RCSAndroid removes a specific file as root when uninstalling: /system/app/StkDevice.apk
  * source: https://github.com/hackedteam/core-android/blob/master/RCSAndroid/src/com/android/dvci/action/UninstallAction.java#L109
  
* android exploit writes 'shell' file to /system/bin/ntpsvd
 * source: https://github.com/hackedteam/core-android/blob/master/RCSAndroid/jni/exploit.c#L739

* RCSAndroid second shell binary: /system/bin/rilcap
  source: https://github.com/hackedteam/core-android/blob/master/RCSAndroid/jni/selinux_suidext/suidext.c#L151
