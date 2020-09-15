import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Radio} from '../../models/Radio';
import {Injectable} from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class RadioRepository {
  private httpClient: HttpClient;

  private webAPIUrl = 'http://localhost:5000/api/';

  constructor(httpClient: HttpClient) {
    this.httpClient = httpClient;
  }

  public async getRadios(): Promise<Array<Radio>> {
    try {
      const url = this.webAPIUrl + 'radios';

      const headers: HttpHeaders = new HttpHeaders()
        .set('accept', 'application/json');

      const response: Array<Radio> =
        await this.httpClient.get<Array<Radio>>(url, {headers: headers})
          .toPromise();

      return response;
    } catch (error) {
      console.log('Error: ' , error);
    }
  }

  public async playRadio(num: number): Promise<any> {
    try {
      const url = this.webAPIUrl + 'radios/' + num + '/play';

      const headers: HttpHeaders = new HttpHeaders()
        .set('accept', 'application/json');

      const response: any =
      await this.httpClient.get(url, {headers: headers})
          .toPromise();

      return response;
    } catch (error) {
      console.log('Error: ' , error);
    }
  }

  public async stopRadio(num: number): Promise<any> {
    try {
      const url = this.webAPIUrl + 'radios/' + num + '/stop';

      const headers: HttpHeaders = new HttpHeaders()
        .set('accept', 'application/json');

      const response: any =
        await this.httpClient.get(url, {headers: headers})
          .toPromise();

      return response;
    } catch (error) {
      console.log('Error: ' , error);
    }
  }
}
