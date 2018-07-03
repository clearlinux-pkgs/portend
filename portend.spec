#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : portend
Version  : 2.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/51/8a/b283d250525e797dbc70f923f1e841c52fd9fd3d97aa4cc3637ec4701150/portend-2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/51/8a/b283d250525e797dbc70f923f1e841c52fd9fd3d97aa4cc3637ec4701150/portend-2.2.tar.gz
Summary  : TCP port monitoring utilities
Group    : Development/Tools
License  : MIT
Requires: portend-python3
Requires: portend-python
Requires: tempora
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : setuptools_scm-python
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/portend.svg
:target: https://pypi.org/project/portend

%package python
Summary: python components for the portend package.
Group: Default
Requires: portend-python3

%description python
python components for the portend package.


%package python3
Summary: python3 components for the portend package.
Group: Default
Requires: python3-core

%description python3
python3 components for the portend package.


%prep
%setup -q -n portend-2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528566534
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
