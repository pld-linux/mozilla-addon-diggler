Summary:	Clear location button next to the location bar
Summary(pl):	Przycisk do usuwania informacji o adresie strony
Name:		mozilla-addon-diggler
%define		_realname	diggler
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.mozdev.org/%{_realname}/%{_realname}-%{version}.xpi
# Source0-md5:	d1d20959032ddc76b460a9d5342cb5a8
Source1:	%{_realname}-installed-chrome.txt
URL:		http://diggler.mozdev.org/
BuildRequires:	unzip
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _chromedir      %{_libdir}/mozilla/chrome

%description
Diggler is a simple add-on to the navigator functionality in Mozilla. It
adds a clear location button next to the location bar much like the one in
Konqueror. It also has a drop down menu with some more useful actions such
as being able to navigate to parent directories in URLs. This feature is
especially handy for FTP operations.

%description -l pl
Diggler to ma³y dodatek do funkcjonalno¶ci przegl±darki w Mozilli.
Dodaje przycisk czyszcz±cy informacjê o adresie strony zaraz obok tego
paska - podobnie jak jest to w Konquerorze. Ma tak¿e rozwijane menu z
u¿ytecznymi funkcjami, takimi jak przechodzenie do katalogów
nadrzêdnych w URL-ach. Jest to przydatne zw³aszcza przy operacjach na
FTP.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

mv $RPM_BUILD_ROOT%{_chromedir}/chrome/%{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
