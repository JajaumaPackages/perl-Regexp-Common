Name: 		perl-Regexp-Common
Version: 	2.120
Release: 	6%{?dist}
Summary: 	Regexp::Common Perl module
License: 	Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Regexp-Common/
Source0: 	http://www.cpan.org/authors/id/A/AB/ABIGAIL/Regexp-Common-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
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
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc TODO README
%{perl_vendorlib}/Regexp
%{_mandir}/man3/*

%changelog
* Wed Aug 29 2007 Ralf Corsépius <rc040203@freenet.de> - 2.120-6
- BR: perl(ExtUtils::MakeMaker).

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 2.120-5
- Mass rebuild.

* Sat Feb 25 2006 Ralf Corsépius <rc040203@freenet.de> - 2.120-4
- Rebuild for FC5/perl-5.8.8.

* Thu Aug 20 2005 Ralf Corsepius <ralf@links2linux.de> - 2.120-3
- Further spec cleanup.

* Thu Aug 20 2005 Ralf Corsepius <ralf@links2linux.de> - 2.120-2
- Spec cleanup.

* Thu Aug 11 2005 Ralf Corsepius <ralf@links2linux.de> - 2.120-1
- FE submission.
