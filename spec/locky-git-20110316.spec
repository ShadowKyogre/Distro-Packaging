Name: locky-git
Version: 20110316
Release: 1%{?dist}
Summary: Locks all X sessions upon suspend or hibernate with xscreensaver or a custom command.
License: GPL
URL: https://github.com/ShadowKyogre/Locky
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: git
Requires: xorg-xdpyinfo pm-utils
%description Locks all X sessions upon suspend or hibernate with xscreensaver or a custom command.

%prep
%setup -qn %_builddir/locky-git-20110316 -c %_builddir/locky-git-20110316

%build

    cd "%_builddir";
    if [ -d $_gitname ]; then
        cd $_gitname && git pull origin;
    else
        git clone $_giturl $_gitname;
    fi

%install

    cd %_builddir/$_gitname;
    install -Dm755 67locky %_buildrootdir/etc/pm/sleep.d/67locky;
    install -Dm644 lockyrc %_buildrootdir/etc/lockyrc

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 20110316-1
- Converted PKGBUILD to spec
