Summary:	DevHelp book: cvs
Summary(pl):	Ksi±¿ka do DevHelpa o cvs
Name:		devhelp-book-cvs
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/cvs.tar.gz
# Source0-md5:	8812b7e31d93163c26ba6262a19391ee
URL:		http://www.devhelp.net/
Requires:	devhelp >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about cvs.

%description -l pl
Ksi±¿ka do DevHelpa o cvs.

%prep
%setup -q -c -n cvs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/books/cvs

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/books/cvs/cvs.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/cvs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
