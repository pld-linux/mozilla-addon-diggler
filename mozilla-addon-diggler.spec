Summary:	Clear location button next to the location bar
Summary(pl.UTF-8):	Przycisk do usuwania informacji o adresie strony
Name:		mozilla-addon-diggler
%define		_realname	diggler
Version:	0.9b
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.mozdev.org/diggler/%{_realname}-%{version}.xpi
# Source0-md5:	f493ecb3ae1e93cdf7a54079479ddaf0
Source1:	%{_realname}-installed-chrome.txt
URL:		http://diggler.mozdev.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Diggler is a simple add-on to the navigator functionality in Mozilla. It
adds a clear location button next to the location bar much like the one in
Konqueror. It also has a drop down menu with some more useful actions such
as being able to navigate to parent directories in URLs. This feature is
especially handy for FTP operations.

%description -l pl.UTF-8
Diggler to mały dodatek do funkcjonalności przeglądarki w Mozilli.
Dodaje przycisk czyszczący informację o adresie strony zaraz obok tego
paska - podobnie jak jest to w Konquerorze. Ma także rozwijane menu z
użytecznymi funkcjami, takimi jak przechodzenie do katalogów
nadrzędnych w URL-ach. Jest to przydatne zwłaszcza przy operacjach na
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
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
