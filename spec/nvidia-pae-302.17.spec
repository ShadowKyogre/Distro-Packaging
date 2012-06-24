Name: nvidia-pae
Version: 302.17
Release: 1%{?dist}
Summary: NVIDIA drivers for linux.
License: custom
URL: http://www.nvidia.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: linux-pae-headers>=3.4 linux-pae-headers<3.5
Requires: linux-pae>=3.4 linux-pae<3.5 nvidia-utils=302.17-1
%description NVIDIA drivers for linux.

%prep
%setup -qn %_builddir/nvidia-pae-302.17 -c %_builddir/nvidia-pae-302.17

%build

    cd "%_builddir";
    sh "${_pkg}.run" --extract-only;
    cd "${_pkg}/kernel";
    make SYSSRC=/lib/modules/"${_kernver}/build" module

%install

    install -D -m644 "%_builddir/${_pkg}/kernel/nvidia.ko" "%_buildrootdir/lib/modules/${_extramodules}/nvidia.ko";
    install -d -m755 "%_buildrootdir/etc/modprobe.d";
    echo "blacklist nouveau" >> "%_buildrootdir/etc/modprobe.d/nouveau_blacklist-pae.conf";
    sed -i -e "s/EXTRAMODULES='.*'/EXTRAMODULES='${_extramodules}'/" "${startdir}/nvidia.install";
    gzip "%_buildrootdir/lib/modules/${_extramodules}/nvidia.ko"

%files
%defattr(-,root,root,-)
/

%posttrans

    EXTRAMODULES='extramodules-3.4-pae';
    depmod $(cat /lib/modules/$EXTRAMODULES/version);
    echo 'In order to use nvidia module, reboot the system.'

%post

    EXTRAMODULES='extramodules-3.4-pae';
    depmod $(cat /lib/modules/$EXTRAMODULES/version);
    rmmod nvidia || echo 'In order to use the new nvidia module, exit Xserver and unload it manually.'

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 302.17-1
- Converted PKGBUILD to spec
