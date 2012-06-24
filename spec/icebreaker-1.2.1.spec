Name: icebreaker
Version: 1.2.1
Release: 2%{?dist}
Summary: A clone of Jezzball that uses icebergs and penguins. (non-theme support version)
License: GPL
URL: http://mattdm.org/icebreaker/
Source0: http://mattdm.org/icebreaker/1.2.x/icebreaker-1.2.1.tgz
Source1: icebreaker.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: 
Requires: sdl_mixer
%description A clone of Jezzball that uses icebergs and penguins. (non-theme support version)

%prep
%setup -qn %_builddir/icebreaker-1.2.1 -c %_builddir/icebreaker-1.2.1

%build

    cd "%_builddir/$pkgname-$pkgver";
    patch -Np1 -i ../icebreaker.patch || return 1;
    make highscoredir=/var/lib/games prefix=/usr || return 1;
    make prefix=%_buildrootdir/usr install highscoredir=%_buildrootdir/var/lib/games || return 1

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 1.2.1-2
- Converted PKGBUILD to spec
