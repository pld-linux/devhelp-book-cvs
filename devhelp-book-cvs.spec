Summary:	DevHelp book: cvs
Summary(pl):	Ksi±¿ka do DevHelp'a o cvs
Name:		devhelp-book-cvs
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/cvs.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about cvs

%description -l pl
Ksi±¿ka do DevHelp o cvs

%prep
%setup -q -c cvs -n cvs

%build
mv -f book cvs
mv -f book.devhelp cvs.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/cvs
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install cvs.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install cvs/* $RPM_BUILD_ROOT%{_prefix}/books/cvs

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
