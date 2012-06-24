Name: vba-m-gtk-svn
Version: 1102
Release: 1%{?dist}
Summary: Gameboy Advance Emulator combining features of all VBA forks - GTK GUI
License: GPL
URL: http://vba-m.ngemu.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: cmake pkgconfig nasm subversion
Requires: gtkmm sdl glibmm libpng zlib cairo mesa gtkglext gtkglextmm libxv hicolor-icon-theme desktop-file-utils
%description Gameboy Advance Emulator combining features of all VBA forks - GTK GUI

%prep
%setup -qn %_builddir/vba-m-gtk-svn-1102 -c %_builddir/vba-m-gtk-svn-1102

%build

    cd %_builddir;
    if [ -d $_svnmod/.svn ]; then
        ( cd $_svnmod && svn up -r $pkgver );
    else
        svn co $_svntrunk --config-dir ./ -r $pkgver $_svnmod;
        svn co $_svndep --config-dir ./;
    fi;
    msg "Source acquired or request timed out.";
    msg "Starting make...";
    mkdir $_svnmod-build;
    cd $_svnmod-build;
    cmake -DCMAKE_CXX_FLAGS=" -fpermissive" -DCMAKE_INSTALL_PREFIX="/usr" -DDATA_INSTALL_DIR:PATH="share/vbam/gtk" -DENABLE_LINK=OFF ../$_svnmod;
    make

%install

    cd $_svnmod-build;
    make DESTDIR=%_buildrootdir install;
    rm -rf %_builddir/$_svnmod-build

%files
%defattr(-,root,root,-)
/

%posttrans

    update-desktop-database -q;
    gtk-update-icon-cache -q -t -f usr/share/icons/hicolor

%post

    posttrans

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 1102-1
- Converted PKGBUILD to spec
