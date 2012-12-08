%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# NOTE: the word list wrongly uses arabic kaf instead of farsi kaf,
# it is fixed trough a script in the make section (pablo)

%define src_ver 0.11-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Persian
%define languagecode fa
%define lc_ctype fa_IR

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.11.0
Release:       %mkrel 7
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure
#%make

# the word list wrongly uses arabic kaf instead of farsi kaf, fixing it
cat << EOF > fixkaf.sh
#!/bin/bash
cat - | \
  sed 's/ك/ک/g' 
EOF
preunzip -c %{languagecode}.cwl | sh ./fixkaf.sh | (LC_ALL=C sort) > %{languagecode}.wl
aspell  --lang=%{languagecode} create master ./%{languagecode}.rws < %{languagecode}.wl

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright 
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.11.0-5mdv2011.0
+ Revision: 662811
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11.0-4mdv2011.0
+ Revision: 603206
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11.0-3mdv2010.1
+ Revision: 518920
- rebuild

* Sat Jun 27 2009 Isabel Vallejo <isabel@mandriva.org> 0.11.0-2mdv2010.0
+ Revision: 390007
- reupdate to 0.11-0
- update to 0.11-0

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.02.0-6mdv2009.1
+ Revision: 350021
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.02.0-5mdv2009.0
+ Revision: 220375
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.02.0-4mdv2008.1
+ Revision: 182421
- provide enchant-dictionary

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.02.0-2mdv2007.0
+ Revision: 123249
- Import aspell-fa

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.02.0-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.02.0-1mdk
- first version

