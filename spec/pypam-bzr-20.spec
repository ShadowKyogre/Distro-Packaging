Name: pypam-bzr
Version: 20
Release: 4%{?dist}
Summary: A Python interface to the PAM library (configured to build for python3)
License: GPL
URL: https://launchpad.net/ubuntu/precise/+source/python-pam
Source0: 2and3compat.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: bzr
Requires: pam python
%description A Python interface to the PAM library (configured to build for python3)

%prep
%setup -qn %_builddir/pypam-bzr-20 -c %_builddir/pypam-bzr-20

%build

    cd "%_builddir";
    if [[ -d "$_bzrmod" ]]; then
        cd "$_bzrmod" && bzr --no-plugins pull "$_bzrtrunk" -r "$pkgver";
        msg "The local files are updated.";
    else
        bzr --no-plugins branch "$_bzrtrunk" "$_bzrmod" -q -r "$pkgver";
        cd python-pam;
    fi;
    patch -Np1 -i "%_builddir/2and3compat.patch";
    python setup.py build

%install

    cd "%_builddir/python-pam";
    python setup.py install --root="%_buildrootdir"

%files
%defattr(-,root,root,-)
/

%changelog
* Sun Jun 24 2012 Sapphira Armageddos <youremail at domain.ext> 20-4
- Converted PKGBUILD to spec
