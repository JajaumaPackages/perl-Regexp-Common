Name: 		perl-Regexp-Common
Version: 	2.120
Release: 	1%{?dist}
Summary: 	Regexp::Common Perl module
License: 	Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Regexp-Common/
Source0: 	http://www.cpan.org/modules/by-module/Regexp/Regexp-Common-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires:	perl
Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Regexp::Common - Provide commonly requested regular expressions

%prep
%setup -q -n Regexp-Common-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc TODO README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Aug 11 2005 Ralf Corsepius <ralf@links2linux.de> - 1.120-1
- FE submission.

* Mon Mar 21 2005 Ralf Corsepius <ralf@links2linux.de> - 1.120-0.pm.2
- Initial packman version.
- Update to FE standards.
