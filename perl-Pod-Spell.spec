Name:           perl-Pod-Spell
Version:        1.04
Release:        4%{?dist}
Summary:        A formatter for spell-checking POD
Group:          Development/Libraries
License:        Artistic 2.0
URL:            http://search.cpan.org/dist/Pod-Spell/
Source0:        http://www.cpan.org/authors/id/X/XE/XENO/Pod-Spell-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(locale)
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Text::Wrap)
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Pod::Spell is a Pod formatter whose output is good for spell-checking.
Pod::Spell rather like Pod::Text, except that it doesn't put much
effort into actual formatting, and it suppresses things that look like
Perl symbols or Perl jargon (so that your spell-checking program won't
complain about mystery words like "$thing" or "Foo::Bar" or "hashref").

%prep
%setup -q -n Pod-Spell-%{version}
for F in README; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" > "${F}.utf8"
    touch -r "${F}" "${F}.utf8"
    mv "${F}.utf8" "$F"
done
sed -i -e '/^#!/ c #!%{__perl}' bin/podspell

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CONTRIBUTING LICENSE README
%{_bindir}/podspell
%{perl_vendorlib}/Pod/
%{_mandir}/man1/podspell.1*
%{_mandir}/man3/*.3pm*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.04-4
- Mass rebuild 2013-12-27

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 1.04-3
- Do not use env in podspell shebang

* Tue Jun 25 2013 Petr Pisar <ppisar@redhat.com> - 1.04-2
- Specify all dependencies

* Thu May 09 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-1
- 1.04 bump
- Update source URL and BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Petr Pisar <ppisar@redhat.com> - 1.01-15
- Specify all dependencies
- Convert README to UTF-8

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 1.01-13
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.01-11
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-9
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.01-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.01-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-4
- Rebuild for perl 5.10 (again)

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-3
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Mon Dec 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-2
- find: fixed arguments order.

* Sun Dec 17 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-1
- First build.
