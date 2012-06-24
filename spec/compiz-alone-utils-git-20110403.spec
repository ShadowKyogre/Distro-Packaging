Name: compiz-alone-utils-git
Version: 20110403
Release: 1%{?dist}
Summary: A few Compiz Standalone utilities based off of some scripts that come with Openbox.
License: GPL
URL: https://github.com/ShadowKyogre/Compiz-Standalone-Utils
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: git
Requires: 
%description A few Compiz Standalone utilities based off of some scripts that come with Openbox.

%prep
%setup -qn %_builddir/compiz-alone-utils-git-20110403 -c %_builddir/compiz-alone-utils-git-20110403

%build

    cd "%_builddir";
    if [ -d $_gitname ]; then
        cd $_gitname && git pull origin;
    else
        git clone $_giturl $_gitname;
    fi

%install

    cd %_builddir/$_gitname;
    mkdir -p %_buildrootdir/usr/bin;
    mkdir -p %_buildrootdir/{usr/share/xs,etc/X11/s}essions;
    mkdir -p %_buildrootdir/etc/xdg/compiz;
    install -Dm755 autostart.sh %_buildrootdir/etc/xdg/compiz/autostart.sh;
    install -Dm755 compiz-alone-session %_buildrootdir/usr/bin/;
    install -Dm755 xdg-autostart %_buildrootdir/usr/bin/;
    install -Dm644 compiz-alone.desktop %_buildrootdir/etc/X11/sessions/;
    install -Dm644 compiz-alone.desktop %_buildrootdir/usr/share/xsessions/

%files
%defattr(-,root,root,-)
/

%posttrans

    cat  <<-EndOfMessage
Place autostart.sh in ~/.config/compiz
It can be found in /etc/xdg/compiz
EndOfMessage

    /bin/true

%post

    posttrans

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 20110403-1
- Converted PKGBUILD to spec
