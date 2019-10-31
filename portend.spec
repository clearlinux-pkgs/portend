#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : portend
Version  : 2.6
Release  : 16
URL      : https://files.pythonhosted.org/packages/04/98/997f8668b11292f13d3e69fc626232c497228306c764523c5a3a3b59c775/portend-2.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/04/98/997f8668b11292f13d3e69fc626232c497228306c764523c5a3a3b59c775/portend-2.6.tar.gz
Summary  : TCP port monitoring and discovery
Group    : Development/Tools
License  : MIT
Requires: portend-license = %{version}-%{release}
Requires: portend-python = %{version}-%{release}
Requires: portend-python3 = %{version}-%{release}
Requires: tempora
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tempora
BuildRequires : tox
BuildRequires : util-linux
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/portend.svg
:target: https://pypi.org/project/portend

%package license
Summary: license components for the portend package.
Group: Default

%description license
license components for the portend package.


%package python
Summary: python components for the portend package.
Group: Default
Requires: portend-python3 = %{version}-%{release}

%description python
python components for the portend package.


%package python3
Summary: python3 components for the portend package.
Group: Default
Requires: python3-core

%description python3
python3 components for the portend package.


%prep
%setup -q -n portend-2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572545476
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/portend
cp %{_builddir}/portend-2.6/LICENSE %{buildroot}/usr/share/package-licenses/portend/a1474494d96f6ddb3a9a0d767a09871ffc388faf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/portend/a1474494d96f6ddb3a9a0d767a09871ffc388faf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
