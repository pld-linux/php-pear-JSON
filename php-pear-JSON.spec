%define		_class		JSON
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - Simple encoder and decoder for JSON notation
Summary(pl.UTF-8):	%{_pearname} - prosty koder i dekoder dla notacji JSON
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	3
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://mike.teczno.com/JSON.tar.gz
# Source0-md5:	fc2cec5a87fe3d70ecbe0857f30eac94
URL:		http://pear.php.net/pepr/pepr-proposal-show.php?id=198
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Obsoletes:	php-pear-JSON-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a simple encoder and decoder for JSON notation.
It is intended for use with client-side Javascript applications that
make use of HTTPRequest to perform server communication functions -
data can be encoded into JSON notation for use in a client-side
Javascript, or decoded from incoming Javascript requests. JSON format
is native to Javascript, and can be directly eval()'ed with no further
parsing overhead.

%description -l pl.UTF-8
Ten pakiet udostępnia prosty koder i dekoder dla notacji JSON. Jest
przeznaczony do używania z aplikacjami w Javascripcie po stronie
klienta korzystającymi z HTTPRequest do komunikacji z serwerem - dane
mogą być kodowane w notacji JSON do używania z poziomu Javascriptu po
stronie klienta lub dekodowane z przychodzących żądań Javascriptu.
Format JSON jest natywny dla Javascriptu i może być bezpośrednio
wykonany przez eval() bez dalszego przetwarzania.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/tests
install JSON.php $RPM_BUILD_ROOT%{php_pear_dir}
install Test-JSON.php $RPM_BUILD_ROOT%{php_pear_dir}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{php_pear_dir}/JSON.php
