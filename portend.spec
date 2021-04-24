#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : portend
Version  : 2.7.1
Release  : 29
URL      : https://files.pythonhosted.org/packages/53/7f/dc51c3c73f1df9ae75e44a3f912147f0d83ef3a0999306e57ebd3ef2c738/portend-2.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/53/7f/dc51c3c73f1df9ae75e44a3f912147f0d83ef3a0999306e57ebd3ef2c738/portend-2.7.1.tar.gz
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
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/portend.svg
:target: `PyPI link`_
.. image:: https://img.shields.io/pypi/pyversions/portend.svg
:target: `PyPI link`_

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
Provides: pypi(portend)
Requires: pypi(tempora)

%description python3
python3 components for the portend package.


%prep
%setup -q -n portend-2.7.1
cd %{_builddir}/portend-2.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613410994
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/portend
cp %{_builddir}/portend-2.7.1/LICENSE %{buildroot}/usr/share/package-licenses/portend/8e6689d37f82d5617b7f7f7232c94024d41066d1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/portend/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
